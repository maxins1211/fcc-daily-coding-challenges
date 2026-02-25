/*
Given a donor blood type and a recipient blood type, determine whether the donor can give blood to the recipient.

Each blood type consists of:

A letter: "A", "B", "AB", or "O"
And an Rh factor: "+" or "-"
Blood types will be one of the valid letters followed by an Rh factor. For example, "AB+" and "O-" are valid blood types.

Letter Rules:

"O" can donate to other letter type.
"A" can donate to "A" and "AB".
"B" can donate to "B" and "AB".
"AB" can donate only to "AB".
Rh Rules:

Negative ("-") can donate to both "-" and "+".
Positive ("+") can donate only to "+".
Both letter and Rh rule must pass for a donor to be able to donate to the recipient.
*/

function canDonate(donor, recipient) {
    if (donor === "O-") {
        return true;
    }
    const [donorLetter, donorRh] = splitBloodType(donor);
    const [recipientLetter, recipientRh] = splitBloodType(recipient);

    const letterRule = {
        "A": { "A": true, "AB": true },
        "B": { "B": true, "AB": true },
        "AB": { "AB": true },
        "O": { "A": true, "B": true, "AB": true }
    }

    const rhRule = {
        "-": { "+": true, "-": true },
        "+": { "+": true }
    }
    const result = letterRule[donorLetter][recipientLetter] && rhRule[donorRh][recipientRh]
    return result === undefined ? false : true
}

function splitBloodType(bloodType) {
    return [bloodType.substr(0, bloodType.length - 1), bloodType[bloodType.length - 1]]
}