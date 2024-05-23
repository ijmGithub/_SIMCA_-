using System.Windows.Controls;
using SimcaWPF.ViewModels;

namespace SimcaWPF.Views
{
    public partial class MQ135View : UserControl
    {
        private readonly MQ135ViewModel _mq135ViewModel;
        public MQ135View()
        {
            InitializeComponent();
            _mq135ViewModel = new MQ135ViewModel();
            DataContext = _mq135ViewModel;
        }

        // Método para actualizar la concentración de gas
        public void UpdateGasConcentration()
        {
            _mq135ViewModel.UpdateGasConcentration();
        }
    }
}
