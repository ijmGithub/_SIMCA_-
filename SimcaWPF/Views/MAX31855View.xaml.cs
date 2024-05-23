using System.Windows.Controls;
using SimcaWPF.ViewModels;

namespace SimcaWPF.Views
{
    public partial class MAX31855View : UserControl
    {
        private readonly MAX31855ViewModel _max31855ViewModel;
        public MAX31855View()
        {
            InitializeComponent();
            _max31855ViewModel = new MAX31855ViewModel(); // Aquí se asigna el ViewModel al DataContext
            DataContext = _max31855ViewModel;
        }

        // Método para actualizar la temperatura
        public void UpdateTemperature()
        {
            _max31855ViewModel.UpdateTemperature();
        }
    }
}
