const request_url = require("supertest")("https://restful-booker.herokuapp.com");
const assert = require("chai").expect;

describe("Create Booking", function () {
  it("Success Create Booking", async function () {

    const response = await request_url
      .post("/booking")
      .set("Content-Type", "application/json")
      .set('Accept', 'application/json')
      .send({firstname: "Isyroqi", lastname: "Galby", totalprice: 350000, depositpaid: true,
      bookingdates: {checkin: "2023-01-28", checkout: "2023-01-29"}, additionalneeds: "Breakfast"
    });

    assert(response.statusCode).to.eql(200);
    assert(response.body.booking.lastname).to.eql('Galby');
    assert(response.body.booking.totalprice).to.eql(350000);
    assert(response.body.booking.depositpaid).to.eql(true);
    assert(response.body.booking.bookingdates.checkin).to.eql('2023-01-28');
    assert(response.body.booking.bookingdates.checkout).to.eql('2023-01-29');
    assert(response.body.booking.additionalneeds).to.eql('Breakfast');
  });
})
