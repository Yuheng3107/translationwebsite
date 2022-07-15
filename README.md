# Website Layout

### Client-Side
Client Side shall consist of a home page, which displays latest chapters released of all novels on the site.
There will be a Dropdown in the navbar listing all the novels and a link to a page /home/<noveltitle> that displays the sypnosis and chapters (with links) of the novel.

This can be done using templating, where the list of chapters can be passed into the context dictionary to render the page dynamically, so only one template is required for all novels.
