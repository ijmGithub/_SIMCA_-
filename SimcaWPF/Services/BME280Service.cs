using System;
using System.Net.Sockets;
using System.Text;

namespace SimcaWPF.Services
{
    public class BME280Service
    {
        private readonly string serverIpAddress;
        private readonly int serverPort;

        public BME280Service(string serverIpAddress, int serverPort)
        {
            this.serverIpAddress = serverIpAddress;
            this.serverPort = serverPort;
        }

        // Método para obtener los datos del sensor BME280 (temperatura, humedad y presión)
        public SensorData GetSensorData()
        {
            try
            {
                using (TcpClient client = new TcpClient(serverIpAddress, serverPort))
                using (NetworkStream stream = client.GetStream())
                {
                    // Envía una solicitud al servidor
                    byte[] data = Encoding.ASCII.GetBytes("GET_SENSOR_DATA");
                    stream.Write(data, 0, data.Length);

                    // Lee la respuesta del servidor
                    byte[] responseBuffer = new byte[1024];
                    int bytesRead = stream.Read(responseBuffer, 0, responseBuffer.Length);
                    string responseData = Encoding.ASCII.GetString(responseBuffer, 0, bytesRead);

                    // Parsea y devuelve los datos del sensor recibidos del servidor
                    string[] sensorDataParts = responseData.Split(',');
                    if (sensorDataParts.Length == 3 &&
                        double.TryParse(sensorDataParts[0], out double temperature) &&
                        double.TryParse(sensorDataParts[1], out double humidity) &&
                        double.TryParse(sensorDataParts[2], out double pressure))
                    {
                        return new SensorData(temperature, humidity, pressure);
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
                Console.WriteLine($"Error al obtener los datos del sensor BME280: {ex.Message}");
                return null; // O podrías lanzar una excepción en lugar de devolver null
            }
        }

        // Clase para representar los datos del sensor (temperatura, humedad y presión)
        public class SensorData
        {
            public double Temperature { get; }
            public double Humidity { get; }
            public double Pressure { get; }

            public SensorData(double temperature, double humidity, double pressure)
            {
                Temperature = temperature;
                Humidity = humidity;
                Pressure = pressure;
            }
        }
    }
}
