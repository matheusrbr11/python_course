from winotify import Notification, audio

notify = Notification(
    app_id="Nome do Aplicativo", 
    title="Título da Notificação", 
    msg="Mensagem da Notificação",
    duration="short")

notify.set_audio(audio.Reminder, loop=False)
notify.add_actions(label="Botão", launch="https://github.com/matheusrbr11")

notify.show()
