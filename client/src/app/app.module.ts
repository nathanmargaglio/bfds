import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { RestangularModule, Restangular } from 'ngx-restangular';

// Material
import { MatButtonModule } from '@angular/material/button';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatInputModule} from '@angular/material/input';
import {MatFormFieldModule} from '@angular/material/form-field';

import { AppComponent } from './app.component';
import { ButtonComponent } from './button/button.component';

export function RestangularConfigFactory (RestangularProvider) {
  RestangularProvider.setBaseUrl('http://localhost:8000/api');
  RestangularProvider.setRequestSuffix('/');
  RestangularProvider.setResponseExtractor(function(response, operation, what, url) {
    var newResponse;
    if (operation === "getList") {
      newResponse = response.results;
      newResponse.count = response.count;
      newResponse.next = response.next;
      newResponse.previous = response.previous;
    } else {
      newResponse = response;
    }
    return newResponse;
  });
}


@NgModule({
  declarations: [
    AppComponent,
    ButtonComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    RestangularModule,
    RestangularModule.forRoot(RestangularConfigFactory),

    MatButtonModule,
    MatButtonToggleModule,
    MatInputModule,
    MatFormFieldModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
