import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable()
export class EnsureAuthenticatedService implements CanActivate {

  constructor(private router: Router) { }

  public isLogged(): boolean {
    return localStorage.getItem('token') ? true : false;
  }

  canActivate(): boolean {
    if (this.isLogged()) {
      return true;
    }

    this.router.navigateByUrl('/login');
    return false;
  }
}

