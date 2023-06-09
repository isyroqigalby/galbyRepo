Cypress.on('uncaught:exception', (err, runnable) => {
  return false
})
describe('Verify Dashboard Scenario', () => {
  it('Success Open the Dashboard', () => {
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

  it('Success Create New Customer', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Back To Customer List', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get(':nth-child(3) > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty Name', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty Company', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty Address', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty City', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty Phone', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Email')
    .should('be.visible')
    .type('sandi@tes.com')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Create New Customer with Empty Email', () => {
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
    cy.get(':nth-child(4) > .btn')
    .should('be.visible')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi')
    cy.get('#Company')
    .should('be.visible')
    .type('Sayonara')
    cy.get('#Address')
    .should('be.visible')
    .type('Serpong')
    cy.get('#City')
    .should('be.visible')
    .type('Tangerang')
    cy.get('#Phone')
    .should('be.visible')
    .type('08715527523')
    cy.get('.col-md-offset-2 > .btn')
    .should('be.visible')
    .click()
  })

  it('Success Search the Customer', () => {
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
    cy.get('#searching')
    .should('be.visible')
    .type('Sandi')
    cy.get('.container > div > form > .btn')
    .click()
  })

  it('Success Search the Invalid Customer', () => {
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
    cy.get('#searching')
    .should('be.visible')
    .type('Asep')
    cy.get('.container > div > form > .btn')
    .click()
    cy.get('td')
    .should('contain.text', 'No Match')
  })

  it('Success Open the Customer Detail', () => {
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
    cy.get('#searching')
    .should('be.visible')
    .type('Sandi')
    cy.get('.container > div > form > .btn')
    .click()
    cy.get(':nth-child(2) > :nth-child(7) > .btn-outline-info')
    .click()
  })

  it('Success Edit the Customer Detail', () => {
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
    cy.get('#searching')
    .should('be.visible')
    .type('Sandi')
    cy.get('.container > div > form > .btn')
    .click()
    cy.get(':nth-child(3) > :nth-child(7) > .btn-outline-primary')
    .click()
    cy.get('#Name')
    .should('be.visible')
    .type('Sandi Yanuar')
    cy.get('.col-md-offset-2 > .btn')
    .click()
  })
  
  it('Success Delete the Customer', () => {
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
    cy.get('#searching')
    .should('be.visible')
    .type('Sandi')
    cy.get('.container > div > form > .btn')
    .click()
    cy.get(':nth-child(5) > :nth-child(7) > .btn-outline-danger')
    .click()
    cy.get('.btn-outline-danger')
    .click()
  })
})