function formClose(id) {
  document.getElementById(id).classList.add('hidden')
}

function formOpen(id) {
  document.getElementById(id).classList.remove('hidden')
}

function onClickBlank(event, id) {
  if (event.target.classList.contains('black-wrapper')) {
    formClose(id)
  }
}
