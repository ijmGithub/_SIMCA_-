using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;
using System.Configuration; // Agregar este espacio de nombres para acceder a la configuración

namespace SimcaWPF.Services
{
    public class MAX31855Service
    {
        private readonly string _serverIpAddress;
        private readonly int _serverPort;

        public MAX31855Service(string serverIpAddress, int serverPort)
        {
            _serverIpAddress = serverIpAddress;
            _serverPort = serverPort;
        }

        // Método para obtener la temperatura del termopar tipo K
        public double GetTemperature()
        {
            // Aquí podrías implementar la lógica para comunicarte con el hardware del termopar MAX31855
            // y obtener la temperatura real.
            // En este ejemplo, simplemente se genera un valor aleatorio como ejemplo.
            Random random = new Random();
            double temperature = random.NextDouble() * 100; // Temperatura en grados Celsius
            return temperature;
        }

        // Método para obtener la temperatura del termopar tipo K desde un servidor remoto
        public double GetTemperatureFromServer()
        {
            try
            {
                using (TcpClient client = new TcpClient(_serverIpAddress, _serverPort))
                {
                    NetworkStream stream = client.GetStream();
                    byte[] data = Encoding.ASCII.GetBytes("GET_TEMPERATURE");
                    stream.Write(data, 0, data.Length);

                    // Recibe la temperatura como una cadena desde el servidor
                    byte[] buffer = new byte[256];
                    int bytesRead = stream.Read(buffer, 0, buffer.Length);
                    string temperatureString = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                    // Convierte la cadena recibida en un valor de temperatura
                    if (double.TryParse(temperatureString, out double temperature))
                    {
                        return temperature;
                    }
                    else
                    {
                        throw new Exception("No se pudo convertir la temperatura recibida.");
                    }
                }
            }
            catch (Exception ex)
            {
                throw new Exception($"Error al obtener la temperatura desde el servidor: {ex.Message}");
            }
        }
    }
}

