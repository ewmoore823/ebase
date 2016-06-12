class @LoginModel extends EbaseModel
    constructor: ->
        super
        @username  = ko.observable()
        @password = ko.observable()

    submit: =>
        console.log(@username())
        console.log(@password())


