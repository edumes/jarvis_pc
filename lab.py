from mateco import TTS

mod = TTS()

mod.setup_voice('pt-br')

mod.convert("")
mod.speak()


