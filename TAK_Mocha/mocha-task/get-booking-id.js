const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("Get Booking ID", function () {
    it("Success Get Booking ID", async function () {

        const response = await request_url
          .get("/booking")
          .send();
        assert(response.statusCode).to.eql(200);
      });
})
