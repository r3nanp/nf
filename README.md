# 🧾 nf – Automatic NF-e Issuer

A fun and useful project to automate the creation of **NF-e (Nota Fiscal Eletrônica)**.
No more clicking around manually – let the script do it for you! 🎯

---

## 🚀 Getting Started

> ⚠️ **Note:** For my personal use case, credentials are securely stored in [Bitwarden](https://bitwarden.com/).
> Make sure to adapt the script if you're not using Bitwarden.

### 📦 Installation

Clone the repository and install the dependencies:

```
git clone https://github.com/r3nanp/nf.git
cd nf
pip install -r requirements.txt
```

Make sure your Bitwarden CLI is configured and you're logged in:

```
bw login
bw unlock
```

---

## 🧠 How It Works

The script launches a browser instance, logs into the NF-e issuing platform using your credentials, and automatically fills out the form to create a new invoice. 🚀

Here’s a simplified version of what runs under the hood:

```python
def main() -> None:
    """
    This is the main function that will be used to run the script.
    The script is responsible for loading the page, finding the login form,
    authenticating the user, and then creating a new NF-e invoice.
    """

    driver = get_driver()
    login(driver)

if __name__ == "__main__":
    main()
```

---

## 🛠 Features

- ✅ Automatically logs into the NF-e system
- ✅ Secure credential retrieval via Bitwarden
- ✅ Fills out and submits invoice forms
- ✅ Headless or visible browser mode (optional)

---

## 🔐 Security

All credentials are managed using [Bitwarden CLI](https://bitwarden.com/help/cli/), keeping sensitive data out of the codebase.

---

## 📌 Notes

- This project is for educational and personal use only.
- Make sure to comply with the terms of service of any platform you're automating.

---

## 🧑‍💻 Author

Made with 💻 and ☕ by [Renan](https://github.com/r3nanp)

---
