// Creator: WebInspector 537.36

import { sleep } from "k6";
import http from "k6/http";

export const options = {};

export default function main() {
  let response;

  response = http.get(
    "http://192.168.0.219:8080/files?path=test_files%2F100MB-file.tar",
    {
      headers: {
        Host: "192.168.0.219:8080",
        Connection: "keep-alive",
        DNT: "1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent":
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.63",
        Accept:
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
      },
    }
  );

  // Automatically added sleep
  sleep(1);
}