# Phoris

Phoris is a daemon that runs a large language model on Linux hardware without configuration. On first boot it detects available RAM, selects the highest-quality model that fits, downloads it from Hugging Face, and serves it on a local OpenAI-compatible HTTP endpoint. If the hardware changes, Phoris adapts on the next boot without any intervention.

## Motivation

Running a language model on constrained hardware, a Raspberry Pi, an ARM SBC, a headless robot, requires manual decisions: which model, which quantization, which backend flags. These decisions are hardware-specific and break silently when the hardware changes. Phoris makes them automatically and consistently.

## Stack

- `FastAPI`: HTTP server
- `llama-cpp-python`: inference engine
- `psutil`: hardware detection
- `huggingface-hub`: model download

## Status

In development. Not yet functional. The first working version will run on Raspberry Pi 4 and Pi 5 and serve an OpenAI-compatible endpoint on `localhost:8080`. Installation instructions and usage examples will be added at that point.

Progress is tracked in the issues. Feedback on the model selection logic and target hardware is welcome before the first release.

## License

MIT