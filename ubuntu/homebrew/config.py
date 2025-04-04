maintainer = "justwinstuff"
maintainer_email = "justwinstuff@gmail.com"
version = "N/A"
dependencies = ["curl"]
steps = [
  '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
]
uninstall_steps = [
  '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"'
]
