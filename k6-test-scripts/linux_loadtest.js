/*
 * Creator: Firefox 81.0
 * Browser: Firefox 81.0
 */

import { sleep, group } from "k6";
import http from "k6/http";

export const options = {
  //discardResponseBodies: true,
};

export default function main() {
  let response;

  group("page_1 - New Tab", function () {
    response = http.get(
      "http://127.0.0.1:8080/files?path=test_files%2F1000MB-file.tar",
      {
        headers: {
          Host: "127.0.0.1:8080",
          "User-Agent":
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
          Accept:
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Accept-Language": "en-US,en;q=0.5",
          "Accept-Encoding": "gzip, deflate",
          Connection: "keep-alive",
          "Upgrade-Insecure-Requests": "1",
        },
      }
    );
  });

  // Automatically added sleep
  sleep(1);
}
