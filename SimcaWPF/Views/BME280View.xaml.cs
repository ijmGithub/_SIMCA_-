using System.Windows.Controls;
using SimcaWPF.ViewModels;

namespace SimcaWPF.Views
{
    public partial class BME280View : UserControl
    {
        private readonly BME280ViewModel _bme280ViewModel;
        public BME280View()
        {
            InitializeComponent();
            _bme280ViewModel = new BME280ViewModel();
            DataContext = _bme280ViewModel;
        }

        // Método para actualizar los datos del sensor BME280
        public void UpdateSensorValues()
        {
            _bme280ViewModel.UpdateSensorValues();
        }
    }
}