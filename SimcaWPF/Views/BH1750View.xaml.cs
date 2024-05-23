using System.Windows.Controls;
using SimcaWPF.ViewModels;

namespace SimcaWPF.Views
{
    public partial class BH1750View : UserControl
    {
        private readonly BH1750ViewModel _bh1750ViewModel;

        public BH1750View()
        {
            InitializeComponent();
            _bh1750ViewModel = new BH1750ViewModel();
            DataContext = _bh1750ViewModel;
        }

        // Método para actualizar los datos del sensor BH1750
        public void UpdateLuxValue()
        {
            _bh1750ViewModel.UpdateLuxValue();
        }
    }
}
