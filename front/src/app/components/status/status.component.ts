import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.css']
})
export class StatusComponent implements OnInit {

  isLoggedIn = false;

  constructor(private auth: AuthService) { }

  ngOnInit() {
    this.auth.ensureAuthenticatedGet('status')
      .then((user) => {
        if (user.json().success === true) {
          this.isLoggedIn = true;
        }
      });
  }

}
