const request_url = require("supertest")("https://reqres.in/api");
const assert = require("chai").expect;

describe("Create User Functionality", function () {
  it("Success Create User", async function () {

    const response = await request_url
      .post("/users")
      .send({nama: "elvanisa", job: "QA"});

    assert(response.statusCode).to.eql(201);
    //assert(response.body.data).to.eql('data');
    //assert(response.body.message).to.eql('data');
  });
  it.skip("Failed Create User", async function () {

    const response = await request_url
      .post("/users")
      .send({nama: "elvanisa", job: "QA"});

    assert(response.statusCode).to.eql(201);
    //assert(response.body.data).to.eql('data');
    //assert(response.body.message).to.eql('data');
  });
  it("Get List User", async function () {

    const response = await request_url
      .get("/users")
      .send();
    assert(response.statusCode).to.eql(200);
    assert(response.body.page).to.eql(1);
    assert(response.body.total).to.eql(12);
  });
  it("Get Single User", async function () {

    const response = await request_url
      .get("/users/2")
      .send();
    assert(response.statusCode).to.eql(200);
    assert(response.body.data.id).to.eql(2);
    assert(response.body.data.first_name).to.eql("Janet");
    assert(response.body.data.last_name).to.eql("Weaver");
  });
});