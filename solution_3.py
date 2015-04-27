# Find out what other data or metadata you can print out for a a
# revision for an article.
# 
# The answer to this question comes down to the possibily options you
# can give to the "rvprop" parameter to requests. You can find that
# list here: https://www.mediawiki.org/wiki/API:Revisions#Parameters
#
# Here's the list at the writing of writing:
#
# rvprop: Which properties to get for each revision
#     ids: Get both of these IDs: revid, parentid (default) MW 1.11+
#     flags: Whether the revision was a minor edit (default) MW 1.11+
#     timestamp: The date and time the revision was made (default)
#     user: The user who made the revision, as well as userhidden and anon flags (default) MW 1.8
#     userid: User id of revision creator, as well as userhidden and anon flags MW 1.17+
#     sha1: SHA-1 (base 16) of the revision MW 1.19+
#     contentmodel: Content model id of the revision MW 1.21+
#     comment: The edit comment (default)
#     parsedcomment: The edit/log comment in HTML format with wikilinks and section references expanded into hyperlinks MW 1.16
#     size: The size of the revision text in bytes MW 1.11+
#     content: The revision content. If set, the maximum limit will be 10 times as low
#     tags: Any tags for this revision, such as those added by AbuseFilter MW 1.16+

