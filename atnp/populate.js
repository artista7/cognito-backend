const AWS = require("aws-sdk");
const uuidv1 = require("uuid/v3");
const getUuid = require("uuid-by-string");

const { Pool, Client } = require("pg");

var credentials = new AWS.SharedIniFileCredentials({
  profile: "vivek-us-east-1"
});
AWS.config.credentials = credentials;
var docClient = new AWS.DynamoDB.DocumentClient({ region: "us-east-1" });
const pool = new Pool();

// docClient.scan(
//   (params = { TableName: "user-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     // console.log(error, data);
//     // console.log("Converted records", data);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       item["password"] = "password1234";
//       item["username"] = item["userName"];
//       delete item["userName"];
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value);
//         } else {
//           return value;
//         }
//       });
//       var query = `INSERT into users_user ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "student-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     // console.log(error, data);
//     // console.log("Converted records", data);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       delete item["__typename"];
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value);
//         } else {
//           return value;
//         }
//       });
//       var query = `INSERT into student ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "college-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     // console.log(error, data);
//     // console.log("Converted records", data);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       delete item["__typename"];
//       item["location"] = "delhi";
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value);
//         } else {
//           return value;
//         }
//       });
//       var query = `INSERT into college ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "company-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     // console.log(error, data);
//     // console.log("Converted records", data);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       delete item["__typename"];
//       item["location"] = "delhi";
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value);
//         } else {
//           return value;
//         }
//       });
//       var query = `INSERT into company ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "drive-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     // console.log(error, data);
//     // console.log("Converted records", data);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       item["status"] = item["status"] ? item["status"] : "inactive";
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into drive ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         // console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//     (params = { TableName: "drive-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//     function(error, data) {
//       // console.log(error, data);
//       // console.log("Converted records", data);
//       data.Items.forEach(item => {
//         item["id"] = getUuid(item["id"]);
//         item["status"] = item["status"] ? item["status"] : "inactive";
//         Object.keys(item).forEach(key => {
//           if (key.endsWith("Id")) {
//             console.log(key, item[key], getUuid(item[key]));
//             item[key] = getUuid(item[key]);
//           }
//         });
//         delete item["__typename"];
//         //   item["email"] = "abc";
//         var values = Object.values(item);
//         values = values.map(value => {
//           if (typeof value == "object") {
//             return JSON.stringify(value).replace(/'/g, "''");
//           } else {
//             return value.replace(/'/g, "''");
//           }
//         });
//         var query = `INSERT into drive ( "${Object.keys(item).join(
//           '", "'
//         )}" ) values ( '${values.join("', '")}' )`;
//         console.log(query);

//         pool.query(query, (err, res) => {
//           // console.log(err, res);
//         });

//         //   console.log(Object.keys(item).join(","));
//       });
//       // console.log(data.Items[0].metadata);
//     }
//   );

// docClient.scan(
//   (params = { TableName: "job-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       item["requirements"] = item["requirements"]
//         ? item["requirements"]
//         : "requirements";
//       item["description"] = item["description"]
//         ? item["description"]
//         : "description";
//       item["responsibilities"] = item["responsibilities"]
//         ? item["responsibilities"]
//         : "responsibilities";
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into job ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         // console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "companyInDrive-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into companyInDrive ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         // console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "studentInDrive-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     console.log("Number of data items ", data.Items.length);
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into studentInDrive ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         // console.log(err, res);
//         if (err) {
//           console.log(err);
//         }
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "jobOpening-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into jobOpening ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         // console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "resume-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else if (typeof value == "string") {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into resume ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         if (err) {
//           console.log(err);
//         }
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// docClient.scan(
//   (params = { TableName: "resumeOpening-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//   function(error, data) {
//     data.Items.forEach(item => {
//       item["id"] = getUuid(item["id"]);
//       Object.keys(item).forEach(key => {
//         if (key.endsWith("Id")) {
//           console.log(key, item[key], getUuid(item[key]));
//           item[key] = getUuid(item[key]);
//         }
//       });
//       delete item["__typename"];
//       //   item["email"] = "abc";
//       var values = Object.values(item);
//       values = values.map(value => {
//         if (typeof value == "object") {
//           return JSON.stringify(value).replace(/'/g, "''");
//         } else if (typeof value == "string") {
//           return value.replace(/'/g, "''");
//         }
//       });
//       var query = `INSERT into resumeOpening ( "${Object.keys(item).join(
//         '", "'
//       )}" ) values ( '${values.join("', '")}' )`;
//       console.log(query);

//       pool.query(query, (err, res) => {
//         if (err) {
//           console.log(err);
//         }
//         // console.log(err, res);
//       });

//       //   console.log(Object.keys(item).join(","));
//     });
//     // console.log(data.Items[0].metadata);
//   }
// );

// var scanroundTable = async () => {
//   docClient.scan(
//     (params = { TableName: "round-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
//     async function(error, data) {
//       data.Items = await data.Items.sort(function(a, b) {
//         var dateA = new Date(a.createdAt);
//         var dateB = new Date(b.createdAt);
//         return dateA.getTime() - dateB.getTime();
//       });

//       const process = async item => {
//         item["id"] = getUuid(item["id"]);
//         // item["nextRoundId"] = null;
//         delete item["nextRound"];

//         Object.keys(item).forEach(key => {
//           if (key.endsWith("Id")) {
//             // console.log(key, item[key], getUuid(item[key]));
//             item[key] = item[key] ? getUuid(item[key]) : null;
//           }
//         });
//         delete item["__typename"];
//         //   item["email"] = "abc";
//         var values = Object.values(item);
//         values = values.map(value => {
//           if (typeof value == "object") {
//             return JSON.stringify(value).replace(/'/g, "''");
//           } else if (typeof value == "string") {
//             return value.replace(/'/g, "''");
//           }
//         });
//         var query = `INSERT into round ( "${Object.keys(item).join(
//           '", "'
//         )}" ) values ( '${values.join("', '")}' )`;

//         try {
//           var response = await pool.query(query);
//         } catch (error) {
//           console.log(query);
//           console.log(error);
//         }
//       };
//       for (item of data.Items) {
//         console.log(item.createdAt);
//         //   console.log(Object.keys(item).join(","));
//         var a = await process(item);
//       }
//       // console.log(data.Items[0].metadata);
//     }
//   );
// };

// scanroundTable();

var scanroundTable = async () => {
  docClient.scan(
    (params = { TableName: "application-er3i5z2zcbhe3n2smzlaa2dr5i-deveast" }),
    async function(error, data) {
      data.Items = await data.Items.sort(function(a, b) {
        var dateA = new Date(a.createdAt);
        var dateB = new Date(b.createdAt);
        return dateB.getTime() - dateA.getTime();
      });

      const process = async item => {
        item["id"] = getUuid(item["id"]);
        item["nextApplicantId"] = item["nextApplicantId"];
        if (!item["nextApplicantId"]) {
          delete item["nextApplicantId"];
        }
        delete item["nextApplicant"];
        Object.keys(item).forEach(key => {
          if (key.endsWith("Id")) {
            // console.log(key, item[key], getUuid(item[key]));
            item[key] = item[key] ? getUuid(item[key]) : null;
          }
        });
        delete item["__typename"];
        //   item["email"] = "abc";
        var values = Object.values(item);
        values = values.map(value => {
          if (typeof value == "object") {
            return JSON.stringify(value).replace(/'/g, "''");
          } else if (typeof value == "string") {
            return value.replace(/'/g, "''");
          }
        });
        var query = `INSERT into application ( "${Object.keys(item).join(
          '", "'
        )}" ) values ( '${values.join("', '")}' )`;

        try {
          var response = await pool.query(query);
        } catch (error) {
          console.log(query);
          console.log(error);
        }
      };
      for (item of data.Items) {
        console.log(item.createdAt);
        //   console.log(Object.keys(item).join(","));
        var a = await process(item);
      }
      // console.log(data.Items[0].metadata);
    }
  );
};

scanroundTable();
