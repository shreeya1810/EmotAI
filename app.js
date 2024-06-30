import express from "express";
import bodyParser from "body-parser";
import {dirname} from "path";
import {fileURLToPath} from "url";

const app = express();
const port = 1989;

app.use(express.static("./"));

app.use(bodyParser.urlencoded({ extended: true }));
const __dirname=dirname(fileURLToPath(import.meta.url));

app.get("/", (req, res) => {
	res.sendFile(__dirname + "/index.html");
})

app.post("/vision", (req, res)=>{
    res.sendFile(__dirname + "/vision.html");
})

app.listen(port, (err)=>{
    if(err) console.log(err);
    console.log(`Listening on Port ${port}`);
})