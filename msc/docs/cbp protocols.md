protocols:  
\*\*ALL POSITION VALUES ARE ABSOLUTE\*\*  
{type: "endTurn"}  
{type: "place", data: {x: int, y: int, type: string}}  
{type: "editAutoOut", data: {x: int, y: int, active: boolean, newRot: string}}  
{type: "rotate", data: {x: int, y: int, newRot: string}}  
{type: "changeVariant", data: {x: int, y: int, newVariant: string}}  
{type: "delete", data: {x: int, y: int}}  
{type: "queueRepackage", data: {x: int, y: int}}  
{type: "sequence", data: \[{x: int, y: int}, …\]}  
{type: "editMode", data: {x: int, y: int, newMode: string}}  
{type: "changeTargeting", data: {x: int, y: int, newTargeting: \[{x: int, y: int}...\]}}  
{type: "activate", data: {x: int, y: int}}  
{type: "changeRouting", data: {x: int, y: int, newRouting: \[{x: int, y: int}...\]}}  
{