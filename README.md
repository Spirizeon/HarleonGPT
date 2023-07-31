
# Harleon

An OpenAi GPT-3-powered discord bot. made using discord.py

## API Reference


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `TOKEN` | `string` | **Discord Bot token** |
| `openai.api_key` | `string` | **GPT-3 API key**.  |




## Authors

- [@Spirizeon](https://www.github.com/spirizeon)
- [@SiliconPaste](https://www.github.com/siliconpaste)



#### Syntax `?l <question>`


## Run Locally

### Manual installation

```bash
git clone https://github.com/spirizeon/harleongpt
```

Go to the project directory

```bash
pip install -r requirements.txt
```
Add your `openai.api_key` and `TOKEN` in `.env` then run

```bash
python3 main.py 
```
### Docker installation (needs docker installed)
The image can be built from the Dockerfile.

Do add your `openai.api_key` and `TOKEN` in `.env` beforehand.
```bash
docker build . -t harleon-bot
docker run -it harleon
```
