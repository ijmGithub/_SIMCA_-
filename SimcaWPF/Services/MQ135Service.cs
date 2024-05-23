using System;
using System.Net.Sockets;
using System.Text;

namespace SimcaWPF.Services
{
    public class MQ135Service
    {
        private readonly string serverIpAddress;
        private readonly int serverPort;

        public MQ135Service(string serverIpAddress, int serverPort)
        {
            this.serverIpAddress = serverIpAddress;
            this.serverPort = serverPort;
        }

        // Método para obtener la concentración de gas medida por el MQ135
        public double GetGasConcentration()
        {
            try
            {
                using (TcpClient client = new TcpClient(serverIpAddress, serverPort))
                using (NetworkStream stream = client.GetStream())
                {
                    // Envía una solicitud al servidor
                    byte[] data = Encoding.ASCII.GetBytes("GET_GAS_CONCENTRATION");
                    stream.Write(data, 0, data.Length);

                    // Lee la respuesta del servidor
                    byte[] responseBuffer = new byte[1024];
                    int bytesRead = stream.Read(responseBuffer, 0, responseBuffer.Length);
                    string responseData = Encoding.ASCII.GetString(responseBuffer, 0, bytesRead);

                    // Parsea y devuelve la concentración de gas recibida del servidor
                    if (double.TryParse(responseData, out double gasConcentration))
                    {
                        return gasConcentration;
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
                Console.WriteLine($"Error al obtener la concentración de gas: {ex.Message}");
                return double.NaN; // Valor NaN para indicar un error
            }
        }

        // Método para obtener la concentración de gas desde un archivo local
        public double GetGasConcentrationFromFile(string filePath)
        {
            // Aquí podrías implementar la lógica para leer la concentración de gas desde un archivo local.
            // Por ejemplo, podrías leer el valor desde un archivo de texto.
            // En este ejemplo, simplemente se genera un valor aleatorio como ejemplo.
            Random random = new Random();
            double gasConcentration = random.NextDouble() * 100; // Valor de ejemplo (%)
            return gasConcentration;
        }
    }
}
