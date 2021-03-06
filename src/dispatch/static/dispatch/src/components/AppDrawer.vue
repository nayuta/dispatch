<template>
  <v-navigation-drawer app :value="toggleDrawer" clipped>
    <vue-perfect-scrollbar class="drawer-menu--scroll" :settings="scrollSettings">
      <v-list shaped>
        <v-list-item class="px-2">
          <v-btn color="error" rounded to="/incidents/report">
            <v-icon left>error_outline</v-icon>
            Report Incident
          </v-btn>
        </v-list-item>
        <v-list-group
          v-for="item in items"
          :key="item.title"
          v-model="item.active"
          :prepend-icon="item.action"
          no-action
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item v-for="child in item.items" :key="child.title" :to="child.route" exact>
            <v-list-item-content>
              <v-list-item-title v-text="child.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </vue-perfect-scrollbar>
  </v-navigation-drawer>
</template>
<script>
import { mapState } from "vuex"
import VuePerfectScrollbar from "vue-perfect-scrollbar"
export default {
  name: "AppDrawer",
  components: {
    VuePerfectScrollbar
  },
  props: {
    expanded: {
      type: Boolean,
      default: true
    },
    drawWidth: {
      type: [Number, String],
      default: "260"
    }
  },

  data: () => ({
    items: [
      {
        action: "dashboard",
        items: [
          { title: "Incidents", route: "/dashboard/incidents" },
          { title: "Tasks", route: "/dashboard/tasks" }
        ],
        title: "Dashboard"
      },
      {
        action: "error_outline",
        items: [
          { title: "List", route: "/incidents/list" },
          { title: "Tasks", route: "/incidents/tasks" },
          { title: "Feedback", route: "/incidents/feedback" }
        ],
        title: "Incident"
      },
      {
        action: "people",
        items: [
          { title: "Individuals", route: "/contact/individuals" },
          { title: "Teams", route: "/contact/teams" },
          { title: "Services", route: "/contact/services" }
        ],
        title: "Contact"
      },
      {
        action: "book",
        items: [
          { title: "Documents", route: "/knowledge/documents" },
          { title: "Terms", route: "/knowledge/terms" },
          { title: "Definitions", route: "/knowledge/definitions" }
        ],
        title: "Knowledge"
      },
      {
        action: "settings",
        items: [
          { title: "Incident Priorities", route: "/configuration/incidentPriorities" },
          { title: "Incident Types", route: "/configuration/incidentTypes" },
          { title: "Plugins", route: "/configuration/plugins" },
          { title: "Tag Types", route: "/configuration/tagTypes" },
          { title: "Users", route: "/configuration/users" },
          { title: "Workflows", route: "/configuration/workflows" }
        ],
        title: "Configuration"
      }
    ],
    scrollSettings: {
      maxScrollbarLength: 160
    }
  }),
  computed: {
    computeLogo() {
      return "/static/m.png"
    },
    ...mapState("app", ["toggleDrawer"])
  },
  created() {}
}
</script>
