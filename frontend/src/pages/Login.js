import { useState } from "react";
import { login } from "../services/api";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const res = await login({ email, password });
    localStorage.setItem("token", res.data.access_token);
    window.location.reload();
  };

  return (
    <div style={{
      background: "#0f0f0f",
      color: "#00ffcc",
      height: "100vh",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      fontFamily: "monospace"
    }}>
      <h1>⚡ CYBER LOGIN</h1>

      <input placeholder="email"
        onChange={e => setEmail(e.target.value)}
        style={inputStyle}
      />

      <input type="password"
        placeholder="password"
        onChange={e => setPassword(e.target.value)}
        style={inputStyle}
      />

      <button onClick={handleLogin} style={btnStyle}>
        ACCESS SYSTEM
      </button>
    </div>
  );
}

const inputStyle = {
  margin: "10px",
  padding: "10px",
  background: "#111",
  border: "1px solid #00ffcc",
  color: "#00ffcc"
};

const btnStyle = {
  padding: "10px 20px",
  background: "#00ffcc",
  border: "none",
  cursor: "pointer"
};
