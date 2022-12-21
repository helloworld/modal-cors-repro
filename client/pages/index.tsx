import { useState } from "react";

export default function Home() {
  const [response, setResponse] = useState("");

  const makeRequest = async () => {
    const URL = "https://helloworld--modal-cors-repro-fastapi-app.modal.run/",
      name = "Alice";

    const response = await fetch(URL, {
      method: "POST",
      body: JSON.stringify({ name }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    const data = await response.json();
    setResponse(JSON.stringify(data, null, 2));
  };

  return (
    <>
      <button onClick={makeRequest}>Make Request</button>
      <pre>{response}</pre>
    </>
  );
}
