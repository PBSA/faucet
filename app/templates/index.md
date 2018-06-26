The purpose of this page is to document the use of PeerPlays's faucet
**API to register new accounts on PeerPlays**.

## Basic Endpoint

The general endpoint for referral API is available at the currently open
address.

## Path

Both endpoints expect the following path in order to reach the actual
faucet:

    /api/v1/accounts

# Rate Limitations

A single IP may only request a new account once per hour.

# Referral Call

In order to create a new account through this faucet, you need a `POST`
request with a JSON formated body.

## Basic JSON format

     {
         "account":{
             "name":"account-name",
             "owner_key":"PPY5WaszCsqVN9hDkXZPMyiUib3dyrEA4yd5kSMgu28Wz47B3wUqa",
             "active_key":"PPY5TPTziKkLexhVKsQKtSpo4bAv5RnB8oXcG4sMHEwCcTf3r7dqE",
             "memo_key":"PPY5TPTziKkLexhVKsQKtSpo4bAv5RnB8oXcG4sMHEwCcTf3r7dqE",
         }
     }

The `*_key` keys have to be valid public keys for the PeerPlays network!

# Reply

The request's reply will have the following form:

     {
         "account":{
             "name":"account-name",
             "owner_key":"PPY5WaszCsqVN9hDkXZPMyiUib3dyrEA4yd5kSMgu28Wz47B3wUqa",
             "active_key":"PPY5TPTziKkLexhVKsQKtSpo4bAv5RnB8oXcG4sMHEwCcTf3r7dqE",
             "memo_key":"PPY5TPTziKkLexhVKsQKtSpo4bAv5RnB8oXcG4sMHEwCcTf3r7dqE",
             "referrer": "<Name of the referrer account>"
         }
     }
