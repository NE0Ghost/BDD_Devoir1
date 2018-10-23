var MongoClient = require('mongodb').MongoClient;
var URL = "mongodb://localhost:27017/";

MongoClient.connect(URL, function(err, db) {
    var dbo = db.db("pagerank");
    
    var graph =
        [
			{ _id:"A" ,  value:{ site: "A", pagerank: 1, neighbors: ["B", "C"]}},
            { _id:"B",   value:{ site: "B", pagerank: 1, neighbors: ["C"]}},
            { _id:"C",   value:{ site: "C", pagerank: 1, neighbors: ["A"]}},
            { _id:"D",   value:{ site: "D", pagerank: 1, neighbors: ["C"]}},
        ];

    dbo.collection("sites").removeMany();
    dbo.collection("sites").insertMany(graph, {w:1}).then(function () {
        
		var reduce = function(site, list) {
			
			var neighbors = [];
			var pagerank = 0.0;
			var DF = 0.85;
			
			list.forEach(function(pr) {
				if(pr instanceof Array) {
					neighbors = pr;
				} else {
					pagerank += pr;
				}
			});
	
			pagerank = 1 - DF + ( DF * pagerank );
			return { site: site, pagerank: pagerank, neighbors: neighbors };
		};
		
        var map = function () {
			var site = this.value.site;
			var neighbors = this.value.neighbors;
			var pagerank = this.value.pagerank;

			neighbors.forEach(function(neighbor) {
				emit(neighbor, pagerank/neighbors.length);
			});
			
			emit(site, 0);
			emit(site, neighbors);
		};
        
        function pagerankIteration(i, max, callback) {
            dbo.collection("sites").mapReduce(map, reduce, {out: {replace: "sites"}}).then(function (collection) {
                collection.find().toArray().then(function (site){
					site.forEach(function(s){
						console.log("Site: " + s.value.site + "  Pagerank: " + s.value.pagerank + "\tNeighbors: " + s.value.neighbors);
                    });
                    console.log("Nombre d'iterations = " + i + "\n");
					
                    if (i == max) callback();
                    pagerankIteration(i + 1, max, callback);
					
                });
            });
        };
        
        pagerankIteration(0, 20, function end() {
            console.log("End");
            db.close();	//Quick and dirty :-)
        });

        
    });
});