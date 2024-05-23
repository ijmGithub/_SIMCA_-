using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace SimcaWPF.Services
{
    public class DS3231Service
    {
        private readonly string _serverIpAddress;
        private readonly int _serverPort;

        public DS3231Service(string serverIpAddress, int serverPort)
        {
            _serverIpAddress = serverIpAddress;
            _serverPort = serverPort;
        }

        public async Task<DateTime> GetCurrentDateTime()
        {
            try
            {
                using (TcpClient client = new TcpClient(_serverIpAddress, _serverPort))
                {
                    NetworkStream stream = client.GetStream();
                    byte[] data = Encoding.ASCII.GetBytes("GET_DATE_TIME");
                    await stream.WriteAsync(data, 0, data.Length);

                    // Recibe la fecha y hora como una cadena desde el servidor
                    byte[] buffer = new byte[256];
                    int bytesRead = await stream.ReadAsync(buffer, 0, buffer.Length);
                    string dateTimeString = Encoding.ASCII.GetString(buffer, 0, bytesRead);

                    // Convierte la cadena recibida en un objeto DateTime
                    DateTime dateTime;
                    if (DateTime.TryParse(dateTimeString, out dateTime))
                    {
                        return dateTime;
                    }
                    else
                    {
                        throw new Exception("No se pudo convertir la fecha y hora recibida.");
                    }
                }
            }
            catch (Exception ex)
            {
                throw new Exception($"Error al obtener la fecha y hora actual: {ex.Message}");
            }
        }

        public DateTime GetCurrentDateTimeFromFile(string filePath)
        {
            // Aquí podrías implementar la lógica para leer la fecha y hora desde un archivo local.
            // Por ejemplo, podrías leer el valor desde un archivo de texto.
            // En este ejemplo, simplemente se genera una fecha y hora actual como ejemplo.
            return DateTime.Now;
        }
    }
}
