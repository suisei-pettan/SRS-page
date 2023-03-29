import { readFileSync } from "fs";
import { createServer } from "https";
import { Server } from "socket.io";

const httpServer = createServer({
  key: readFileSync("/www/server/panel/ssl/privateKey.pem"),
  cert: readFileSync("/www/server/panel/ssl/certificate.pem")
});

const io = new Server(httpServer, { /* options */
  cors: {
    origin: "https://yagoo2.xn--ujqyjt8y32c5tfri2791a.xyz"
  }
});

io.on("connection", (socket) => {
  socket.on("danmaku", (arg) => {
    var danma = JSON.parse(arg);
    var channel=danma.ch;
    io.emit("danmaku"+channel, arg);
  });
});

httpServer.listen(2083);