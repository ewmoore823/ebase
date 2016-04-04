class @Test
    constructor: ->
        @x = []
        for a in ['0','1','2','3','4','5']
            @x.push(a)

    get_x: =>
        console.log(@x)

