import { POSITION } from 'vue-toastification';

const toastOptions = {
  transition: "Vue-Toastification__fade", // Tipo de transição
  position: POSITION.TOP_CENTER,          // Posição do toast
  timeout: 5000,                          // Duração em ms (5 segundos)
  closeOnClick: true,                     // Fecha ao clicar no toast
  pauseOnFocusLoss: true,                 // Pausa em perda de foco
  pauseOnHover: true,                     // Pausa ao passar o mouse
  draggable: true,                        // Permite arrastar
  draggablePercent: 0.6,                  // Porcentagem para arrastar
  showCloseButtonOnHover: false,          // Botão fechar ao passar o mouse
  hideProgressBar: false,                 // Esconde a barra de progresso
  closeButton: 'button',                  // Personaliza o botão fechar
  icon: true,                             // Exibe ícone padrão
  rtl: false,                             // Direção do texto (LTR ou RTL)
  shareAppContext: true,

};

export default toastOptions;


