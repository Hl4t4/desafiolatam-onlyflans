const alertPlaceholder = document.getElementById('loginAlertPlaceholder')
const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    appendAlert('Tu nombre de usuario y contraseña no son correctos. Intentalo de nuevo.', 'success')
  })
}

document.addEventListener("DOMContentLoaded", function() {
    var modal = document.getElementById('loginErrorModal');
    if (modal && modal.classList) {
        modal.classList.add('show');
        if (modal.classList.contains('fade')) {
            modal.style.display = 'block';
        }
    }
});