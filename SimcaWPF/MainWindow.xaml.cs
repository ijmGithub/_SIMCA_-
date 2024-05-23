using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using SimcaWPF.ViewModels;
using SimcaWPF.Views;

namespace SimcaWPF;

/// <summary>
/// Interaction logic for MainWindow.xaml
/// </summary>
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        // Escuchamos el evento Loaded de la ventana para asegurarnos de que todas las vistas se han inicializado
        Loaded += MainWindow_Loaded;
    }

    // Evento Loaded de la ventana principal
    private async void MainWindow_Loaded(object sender, RoutedEventArgs e)
    {
        // Esperamos un breve tiempo para asegurarnos de que las vistas se han cargado completamente
        await Task.Delay(100);

        // Accedemos a las instancias de las vistas a través de los nombres asignados en el archivo XAML
        var bh1750View = (BH1750View)FindName("BH1750View");
        var bme280View = (BME280View)FindName("BME280View");
        var ds3231View = (DS3231View)FindName("DS3231View");
        var max31855View = (MAX31855View)FindName("MAX31855View");
        var mq135View = (MQ135View)FindName("MQ135View");

        // Iniciar el bucle de actualización cada segundo
        // StartUpdatingLoop(bh1750View, bme280View, ds3231View, max31855View, mq135View);
        StartUpdatingLoop(bh1750View, bme280View, null, max31855View, mq135View);
    }

    // Método para iniciar el bucle de actualización
    private async void StartUpdatingLoop(BH1750View bh1750View, BME280View bme280View, DS3231View ds3231View, MAX31855View max31855View, MQ135View mq135View)
    {
        while (true)
        {
            // Verificar si las instancias no son nulas antes de llamar a los métodos

            // Actualizar los datos de cada sensor
            if (bh1750View != null)
                bh1750View.UpdateLuxValue();
            if (bme280View != null)
                bme280View.UpdateSensorValues();
            if (ds3231View != null)
                ds3231View.UpdateDateTime();
            if (max31855View != null)
                max31855View.UpdateTemperature();
            if (mq135View != null)
                mq135View.UpdateGasConcentration();

            // Esperar un segundo antes de la próxima actualización
            await Task.Delay(1000);
        }
    }
}