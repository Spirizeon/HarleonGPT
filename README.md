
# Harleon-GPT

An OpenAi GPT-3-powered discord bot. made using discord.py, docker and github actions.

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
### Docker run
The image must be pulled from GHCR and run (needs Docker installed and set to `$PATH`) 
```bash
docker pull ghcr.io/spirizeon/harleongpt/harleongpt:latest
docker run -it harleon <openai-key> <token> 
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Discord Bot token** |
| `openai-key` | `string` | **GPT-3 API key**.  |


