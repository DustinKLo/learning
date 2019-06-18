# creating index with percolater
curl -X PUT "localhost:9200/my-index" -H 'Content-Type: application/json' -d'
{
  "mappings": {
    "properties": {
       "message": {
         "type": "text"
       },
       "query": {
         "type": "percolator"
       }
    }
  }
}
' | jq

# adding percolater query
curl -X PUT "localhost:9200/my-index/_doc/1?refresh" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "match" : {
      "message" : "bonsai tree"
    }
  }
}
' | jq


# percolating with given document on percolater index
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "percolate" : {
      "field" : "query",
      "document" : {
        "message" : "A new bonsai tree in the office"
      }
    }
  }
}
' | jq

# Percolating in a filter contextedit
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "constant_score": {
      "filter": {
        "percolate" : {
          "field" : "query",
          "document" : {
            "message" : "A new bonsai tree in the office"
          }
        }
      }
    }
  }
}
' | jq


# percolate multiple documents
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "percolate" : {
      "field" : "query",
      "documents" : [ 
        {
          "message" : "bonsai tree"
        },
        {
          "message" : "new tree"
        },
        {
          "message" : "the office"
        },
        {
          "message" : "office tree"
        }
      ]
    }
  }
}
' | jq


# adding new document to percolate against
curl -X PUT "localhost:9200/my-index2/_doc/2" -H 'Content-Type: application/json' -d'
{
  "message" : "A new bonsai tree in the office"
}
' | jq

# percolating with existing document
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "percolate" : {
      "field": "query",
      "index" : "my-index2",
      "id" : "test_id1",
      "version" : 1 
    }
  }
}
' | jq


# adding data to test highlighting percolater query
curl -X PUT "localhost:9200/my-index/_doc/3?refresh" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "match" : {
      "message" : "brown fox"
    }
  }
}
' | jq

# adding data to test highlighting percolater query
curl -X PUT "localhost:9200/my-index/_doc/4?refresh" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "match" : {
      "message" : "lazy dog"
    }
  }
}
' | jq


# highlighting percolater query
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "percolate" : {
      "field": "query",
      "document" : {
        "message" : "The quick brown fox jumps over the lazy dog"
      }
    }
  },
  "highlight": {
    "fields": {
    "message": {}
    }
  }
}
' | jq


# multiple percolate queries
curl -X GET "localhost:9200/my-index/_search" -H 'Content-Type: application/json' -d'
{
  "query" : {
    "bool" : {
      "should" : [
        {
          "percolate" : {
            "field" : "query",
            "document" : {
              "message" : "bonsai tree"
            },
            "name": "query1" 
          }
        },
        {
          "percolate" : {
            "field" : "query",
            "document" : {
              "message" : "tulip flower"
            },
            "name": "query2" 
          }
        }
      ]
    }
  }
}
' | jq

