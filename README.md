# 📝 AI Content Generator using OpenAI GPT-3.5

This Streamlit web app allows users to generate custom-written content such as blog posts, tweets, and product descriptions using OpenAI GPT-3.5.

## Features

- Choose content type (blog, tweet, ad copy, etc.)
- Control tone and length
- Uses GPT-3.5 via OpenAI API
- Lightweight and within $5 free usage tier

## Setup

1. Install dependencies:

```bash
pip install openai streamlit python-dotenv
```

2. Create a `.env` file in the root with your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

3. Run the app:

```bash
streamlit run app/app.py
```

## License

MIT
