# SOLOQ POLICE:

![Test Image 4](https://cdn.discordapp.com/attachments/783997102996979733/943096797201588255/discordpolice.png)

## DISCLAIMER

* I don't consider myself good at coding, in fact this script is really not optimized, but at least it works. (if you can help me make it cleaner/better PM me)
* **Why did you create this bot ?** As a coach I feel like a lot of the time players are slacking in soloQ. And I cba'd counting every players games everyday on opgg, now I can do that with a simple command.
* **How did you create this bot ?** Using really basic League API & Python knowledge.
* **Who are you** ? I am Aries, coach for Team Oplon in the LFL

My Twitter:
https://twitter.com/arieslol_

## Installation

The installation of the bot is fairly easy if you have programming knowledge, if you don't then it's longer, so I will do it for both:

## Installation (if you know how Python/League API)💻

* From the Discord developer website, create an application & a bot, follow this tutorial: https://betterprogramming.pub/coding-a-discord-bot-with-python-64da9d6cade7
* Once your discord bot is loaded on your Team server, here are things that you need to modify in our python script:
`api_key = 'INSERT API KEY HERE' # here please put in-between the quotes your Riot API Developer Key` (line 11)
`top_id = 'fQwRacUndeCleiOeQi4qm4WTFuoqSZg7SXnQWeAepWZPZ6teQ7Aytl5wAoAG3ltsM_ZcNT904BbIUg' # here write the puuid of your toplaner
jgl_id = 'Kae9k0d4l2o6sKblB36Pm-IuPjgDNFLu2Vz0ODNcOG2PaNVXRWL27j82I7-UKGCwDgifz82RrT6zQA' # here write the puuid of your jungler
mid_id = '4B_9lFf5JU4onY__sQyZY6RVVNrXnsCsX6vqYgjWKjlFqnGj4Vb0gxCa0mUMWU8uK_6NM-IeqaB_ag' # here write the puuid of your midlaner
adc_id = 'eCze5I2zMSyG4x84qyVrlbJjQOdyr6cn6IPah6AOjpZA7x6LBm4EtdMUJzjR8EAZBazCsGqSy7-oTw' # here write the puuid of your ad carry
sup_id = 'IQYpa2gn6ocPcdte-LHXNk8VTVSrcFY6EzfJqux4Nw33wonDXugp6bChZm3bY5-hC2d-2g_17HfMGg' # here write the puuid of your support`
Here insert puuids of your five players, if you don't know how to find them, learn more here: https://developer.riotgames.com/apis#summoner-v4/GET_getBySummonerName


## Usage

### Screenshots

### Features

## Code

[![Build Status](https://qa.nuxeo.org/jenkins/buildStatus/icon?job=/nuxeo/addons_nuxeo-sample-project-master)](https://qa.nuxeo.org/jenkins/job/nuxeo/job/addons_nuxeo-sample-project-master/)

### Content

Description, sub-modules organization...

### Requirements

See [CORG/Compiling Nuxeo from sources](http://doc.nuxeo.com/x/xION)

Sample: <https://github.com/nuxeo/nuxeo/blob/master/nuxeo-distribution/README.md>

### Limitations

Sample: <https://github.com/nuxeo-archives/nuxeo-features/tree/master/nuxeo-elasticsearch>

### Build

    mvn clean install

Build options:

* ...

### Deploy (how to install build product)

Direct to MP package if any. Otherwise provide steps to deploy on Nuxeo Platform:

 > Copy the built artifacts into `$NUXEO_HOME/templates/custom/bundles/` and activate the `custom` template.

## Resources (Documentation and other links)

## Contributing / Reporting issues

Link to JIRA component (or project if there is no component for that project). Samples:

* [Link to component](https://jira.nuxeo.com/issues/?jql=project%20%3D%20NXP%20AND%20component%20%3D%20Elasticsearch%20AND%20Status%20!%3D%20%22Resolved%22%20ORDER%20BY%20updated%20DESC%2C%20priority%20DESC%2C%20created%20ASC)
* [Link to project](https://jira.nuxeo.com/secure/CreateIssue!default.jspa?project=NXP)

## License

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

## About Nuxeo

Nuxeo Platform is an open source Content Services platform, written in Java. Data can be stored in both SQL & NoSQL databases.

The development of the Nuxeo Platform is mostly done by Nuxeo employees with an open development model.

The source code, documentation, roadmap, issue tracker, testing, benchmarks are all public.

Typically, Nuxeo users build different types of information management solutions for [document management](https://www.nuxeo.com/solutions/document-management/), [case management](https://www.nuxeo.com/solutions/case-management/), and [digital asset management](https://www.nuxeo.com/solutions/dam-digital-asset-management/), use cases. It uses schema-flexible metadata & content models that allows content to be repurposed to fulfill future use cases.

More information is available at [www.nuxeo.com](https://www.nuxeo.com).
