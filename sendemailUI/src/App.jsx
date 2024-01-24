import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import axios from "axios";

function App() {
  const [Subject, setSubject] = useState("");
  const [From, setFrom] = useState("todentsukanai@gmail.com");
  const [To, setTTo] = useState([""]);
  const [Cc, setCc] = useState([""]);
  const [Bcc, setBcc] = useState([""]);
  const [Content, setContent] = useState("");

  const log = () => {
    console.log("Subject", Subject);
    console.log("From", From);
    console.log("To", To);
    console.log("Cc", Cc);
    console.log("Bcc", Bcc);
    console.log("Content", Content);

    const data = {
      Subject,
      From,
      To: To.join(','),
      Cc: Cc.join(','),
      Bcc: Bcc.join(','),
      Content
    }

    console.log(JSON.stringify(data));

    axios.post('http://127.0.0.1:8000/email/', data)
  }

  return (
    <>
      <div>
        <h1>Send Email</h1>
        <div>
          <label>Subject: </label>
          <input name="Subject" value={Subject} onChange={e => setSubject(e.target.value)} />
        </div>
        <div>
          <label>From: </label>
          <input required readOnly name="From" value={From} />
        </div>
        {To.map((to, index) => (
          <div>
            <label>To: </label>
            <input required name="To" defaultValue={to} onChange={(e) => {
              let newTo = To;
              newTo[index] = e.target.value;
              setTTo(newTo)
            }}/>
          </div>
        ))}
        <button onClick={() => {setTTo([...To, ""])}}>Add to</button>

        {Cc.map((cc, index) => (
          <div>
            <label>Cc: </label>
            <input required name="Cc" defaultValue={cc} onChange={(e) => {
              let newCc = Cc;
              newCc[index] = e.target.value;
              setCc(newCc)
            }}/>
          </div>
        ))}
        <button onClick={() => {setCc([...Cc, ""])}}>Add cc</button>

        {Bcc.map((bcc, index) => (
          <div>
            <label>Bcc: </label>
            <input required name="Bcc" defaultValue={bcc} onChange={(e) => {
              let newBcc = Bcc;
              newBcc[index] = e.target.value;
              setBcc(newBcc)
            }}/>
          </div>
        ))}
        <button onClick={() => {setBcc([...Bcc, ""])}}>Add bcc</button>

        <div>
          <label>Content</label>
          <textarea name="Content" onChange={e => setContent(e.target.value)} value={Content}></textarea>
        </div>
        <button onClick={log}>Send Email</button>
      </div>
    </>
  );
}

export default App;
