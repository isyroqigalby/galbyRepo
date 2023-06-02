const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("Get Booking", function () {
    it("Success Get Booking", async function () {

        const response = await request_url
          .get("/booking/475")
          .set('Accept', 'application/json')
          .send();
        assert(response.statusCode).to.eql(200);
      });
})
