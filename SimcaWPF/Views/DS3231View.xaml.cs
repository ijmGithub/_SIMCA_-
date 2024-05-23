using System.Windows.Controls;
using SimcaWPF.ViewModels;

namespace SimcaWPF.Views
{
    public partial class DS3231View : UserControl
    {
        private readonly DS3231ViewModel _ds3231ViewModel;
        public DS3231View()
        {
            InitializeComponent();
            _ds3231ViewModel = new DS3231ViewModel();
            DataContext = _ds3231ViewModel;
        }

        // Método para actualizar la fecha y hora
        public void UpdateDateTime()
        {
            _ds3231ViewModel.UpdateDateTime();
        }
    }
}
