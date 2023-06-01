Cypress.on('uncaught:exception', (err, runnable) => {
  return false
})
describe('Verify Login-Logout Scenario', () => {
  it('Success Login with Existing Account', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('satpamlucu')
    cy.get('#Password')
    .should('be.visible')
    .type('NyobaDoangIni1')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
  })

  it('Success Login with Uppercase Username when the Existing Username are in Lowercase', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('SATPAMLUCU')
    cy.get('#Password')
    .should('be.visible')
    .type('NyobaDoangIni1')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
  })

  it('Success Login with Uppercase Password when the Existing Password are mixed of Uppercase and Lowercase', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('SATPAMLUCU')
    cy.get('#Password')
    .should('be.visible')
    .type('NYOBADOANGINI1')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
  })

  it('Success Open Register Page when User Try to Login but Does Not Have an Account', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('.btn > a').click()
  })

  it('Success Clear the Username and Password', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('SATPAMLUCU')
    cy.get('#Password')
    .should('be.visible')
    .type('NYOBADOANGINI1')
    cy.get(':nth-child(7) > :nth-child(2) > .btn-secondary')
    .should('be.visible')
    .click()
  })

  it('Failed Login with Wrong Username', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('bekassampah')
    cy.get('#Password')
    .should('be.visible')
    .type('NyobaDoangIni1')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
    cy.get('.alert-danger')
    .should('contain.text', 'Wrong username or password')
  })

  it('Failed Login with Wrong Password', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('satpamlucu')
    cy.get('#Password')
    .should('be.visible')
    .type('NyobaDoangInitestestes')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
    cy.get('.alert-danger')
    .should('contain.text', 'Wrong username or password')
  })

  it('Failed Login with Empty Username', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Password')
    .should('be.visible')
    .type('NyobaDoangInitestestes')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
    cy.get('.alert-danger')
    .should('contain.text', 'Wrong username or password')
  })

  it('Failed Login with Empty Password', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('satpamlucu')
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
    cy.get('.alert-danger')
    .should('contain.text', 'Wrong username or password')
    cy.get('.field-validation-error')
    .should('contain.text', 'Please enter password')
  })

  it('Failed Login After User Clear the Username and Password', () => {
    cy.visit('https://itera-qa.azurewebsites.net/')
    cy.get('.form-inline > .navbar-nav > :nth-child(2) > .nav-link').click()
    cy.get('#Username')
    .should('be.visible')
    .type('SATPAMLUCU')
    cy.get('#Password')
    .should('be.visible')
    .type('NYOBADOANGINI1')
    cy.get(':nth-child(7) > :nth-child(2) > .btn-secondary')
    .should('be.visible')
    .click()
    cy.get('.btn-primary')
    .should('be.visible')
    .click()
    cy.get('.alert-danger')
    .should('contain.text', 'Wrong username or password')
    cy.get('.field-validation-error')
    .should('contain.text', 'Please enter password')
  })
})