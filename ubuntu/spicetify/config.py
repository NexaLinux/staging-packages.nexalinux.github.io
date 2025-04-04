maintainer = "komaru.yml"
maintainer_email = "winbo.yml@proton.me"
version = "N/A"
dependencies = ["curl", "dash"]
steps = [
  'curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh',
  '~/.spicetify/spicetify backup apply'
]
uninstall_steps = [
  'spicetify restore',
  'rm -rf ~/.spicetify'
]
