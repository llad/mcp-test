# MCP Test

This project aims to create a simple MCP (Multi-Component Platform) server with a publicly accessible API for experimentation and understanding of its core components.

## Project Plan

1. **MCP Server**
   - Build a minimal MCP server exposing a public API.
   - Focus on clarity and ease of understanding for each component.
   - Allow users to submit a URL to a GICS CSV file and process its contents.

2. **Jupyter Notebook Client**
   - Create a Jupyter notebook that connects to the MCP server.
   - Use the MCP server as part of a request to the OpenAI API.
   - Enable interactive chat with the content managed by the MCP server.

## Goals

- Learn and demonstrate the main architectural components of an MCP server.
- Provide an example of integrating the MCP server with a Jupyter notebook and the OpenAI API.
- Encourage experimentation and extension.

## Getting Started

1. **Run the MCP Server**
    - Set an API key in the environment:
      ```bash
      export MCP_API_KEY="secret-key"
      python server.py
      ```
    - The server requires the key to be sent in the `X-API-Key` header.

2. **Use the Jupyter Notebook**
    - The notebook reads `MCP_API_KEY` from the environment and uses it when calling the server.

## License

MIT License.

---
*This project is for educational and prototyping purposes.*
