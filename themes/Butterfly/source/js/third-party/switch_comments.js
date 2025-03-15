$('#switch-comment').click(function () {
  switchComment()
  return false
})
function switchComment() {
  const title = $('#switch-comment').attr('title') === '切换为Gitalk' ? '切换为Valine' : '切换为Gitalk'
  const i = $('#switch-comment>i')
  if ($('#gitalk-container').css('display') === 'none') {
    $('#vcomment').slideUp('normal', () => {
      $('#gitalk-container').slideDown('normal', () => {
        $('#switch-comment').attr('title', title)
        i.hasClass('fa-toggle-off') ? i.removeClass('fa-toggle-off').addClass('fa-toggle-on') : i.removeClass('fa-toggle-on').addClass('fa-toggle-off')
      })
    })
  } else {
    $('#gitalk-container').slideUp('normal', () => {
      $('#vcomment').slideDown('normal', () => {
        $('#switch-comment').attr('title', title)
        i.hasClass('fa-toggle-off') ? i.removeClass('fa-toggle-off').addClass('fa-toggle-on') : i.removeClass('fa-toggle-on').addClass('fa-toggle-off')
      })
    })
  }
}