# 🔡 Text Encoder & Decoder (Code/Debug Tool)

A simple Python script to **encode** or **decode** text using a custom logic.  
Great for educational purposes, learning string manipulation, and understanding basic command-line interaction.

---

## 📌 Features

- **Code Mode**: Applies a custom transformation to each word:
  - For words with 3 or more characters, it scrambles and extends the word.
  - Shorter words are simply reversed.
- **Debug Mode**: Reverses the transformation:
  - Extracts and reconstructs the original word from the encoded format.
  - Short words are reversed again to retrieve the original.

---

## ⚙️ How It Works

### `coding(text)`
Encodes input text word by word:
- If word length ≥ 3:
  - New form = `i[2] + i[0] + i[1] + i[-1] + i[1:-1] + i[0] + i[0:3]`
- If word length < 3:
  - Reverse the word

### `debugging(text)`
Decodes previously encoded text:
- If word length ≥ 3:
  - Remove first 3 and last 3 characters from the word
  - Reconstruct original word using `last_char + middle + first_char`
- If word length < 3:
  - Reverse the word


