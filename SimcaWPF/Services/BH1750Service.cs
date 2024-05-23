using System;
using System.Net.Sockets;
using System.Text;

namespace SimcaWPF.Services
{
    public class BH1750Service
    {
        private readonly string _serverIpAddress;
        private readonly int _serverPort;

        public BH1750Service(string serverIpAddress, int serverPort)
        {
            _serverIpAddress = serverIpAddress;
            _serverPort = serverPort;
        }

        // Método para obtener la intensidad de luz ambiental del sensor BH1750 desde el servidor Python
        public double GetLightIntensity()
        {
            try
            {
                using (TcpClient client = new TcpClient(_serverIpAddress, _serverPort))
                using (NetworkStream stream = client.GetStream())
                {
                    // Envía una solicitud al servidor para obtener la intensidad de luz ambiental
                    byte[] data = Encoding.ASCII.GetBytes("GET_LIGHT_INTENSITY");
                    stream.Write(data, 0, data.Length);

                    // Lee la respuesta del servidor
                    byte[] responseBuffer = new byte[1024];
                    int bytesRead = stream.Read(responseBuffer, 0, responseBuffer.Length);
                    string responseData = Encoding.ASCII.GetString(responseBuffer, 0, bytesRead);

                    // Parsea y devuelve la intensidad de luz ambiental recibida del servidor
                    if (double.TryParse(responseData, out double lightIntensity))
                    {
                        return lightIntensity;
                    }
                    else
                    {
                        throw new Exception("Respuesta no válida recibida del servidor.");
                    }
                }
            }
            catch (Exception ex)
            {
                // Manejo de errores (por ejemplo, registro, notificación al usuario, etc.)
                Console.WriteLine($"Error al obtener la intensidad de luz ambiental: {ex.Message}");
                return double.NaN; // Valor NaN para indicar un error
            }
        }
    }
}
